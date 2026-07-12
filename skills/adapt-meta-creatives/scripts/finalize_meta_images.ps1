param(
    [Parameter(Mandatory=$true)][string]$InputPath,
    [Parameter(Mandatory=$true)][string]$OutputPath,
    [Parameter(Mandatory=$true)][ValidateSet('1080x1080','1080x1350','1080x1920')][string]$Size
)

Add-Type -AssemblyName System.Drawing

$dimensions = @{
    '1080x1080' = @(1080, 1080)
    '1080x1350' = @(1080, 1350)
    '1080x1920' = @(1080, 1920)
}

$targetWidth, $targetHeight = $dimensions[$Size]
$parent = Split-Path -Parent $OutputPath
if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }

$image = [System.Drawing.Image]::FromFile((Resolve-Path $InputPath))
$scale = [Math]::Min($targetWidth / $image.Width, $targetHeight / $image.Height)
$drawWidth = [Math]::Round($image.Width * $scale)
$drawHeight = [Math]::Round($image.Height * $scale)
$x = [Math]::Floor(($targetWidth - $drawWidth) / 2)
$y = [Math]::Floor(($targetHeight - $drawHeight) / 2)

$bitmap = New-Object System.Drawing.Bitmap($targetWidth, $targetHeight)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.Clear(([System.Drawing.Bitmap]$image).GetPixel(2, 2))
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$graphics.DrawImage($image, $x, $y, $drawWidth, $drawHeight)
$bitmap.Save($OutputPath, [System.Drawing.Imaging.ImageFormat]::Png)

$graphics.Dispose()
$bitmap.Dispose()
$image.Dispose()

