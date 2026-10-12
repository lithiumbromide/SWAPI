---
title: "IRenderNotificationHandler2 Interface"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler2"
member: ""
kind: "interface"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2.html"
---

# IRenderNotificationHandler2 Interface

Allows access to the render notification handler.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IRenderNotificationHandler2
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler2
```

### C#

```csharp
public interface IRenderNotificationHandler2
```

### C++/CLI

```cpp
public interface class IRenderNotificationHandler2
```

## VBA Syntax

See [IRenderNotificationHandler2](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderNotificationHandler2.html).

## Examples

The following C# class demonstrates how to implement IRenderNotificationHandler2 which supports two callbacks, OnPreviewRequested and OnRenderActionRequested. Note that this code is part of a larger add-in which is posted in the SOLIDWORKS API Support Knowledge Base (**SOLIDWORKS Visualize API Sample Plugin (C#)**):

=======================================

using System.IO;

using System.Timers;

using System.Windows.Forms;

using System.Windows.Media;

using System.Windows.Media.Imaging;

using Shared;

using SolidWorks.Visualize.Interfaces;

using PixelFormat = System.Windows.Media.PixelFormat;

using Timer = System.Timers.Timer;

namespace SWVizAPISample2

{

public class RenderHandler2 : **IRenderNotificationHandler2**

{

private readonly Timer _requestPreviewTimer;

private bool _previewRequestPending = false;

private IRenderCallbackHandler _callbackHandler;

public RenderHandler2()

{

_requestPreviewTimer = new Timer(5000); // every 5s

_requestPreviewTimer.Elapsed += RequestPreview;

RenderProgressDialog = new OutputViewerDialog("Output Viewer Dialog");

RenderProgressDialog.ViewModel.RenderCanceled += CancelRender;

RenderProgressDialog.ViewModel.RenderCanceledAndSave += CancelAndSaveRender;

}

public OutputViewerDialog RenderProgressDialog { get; }

public Stream BitmapSourceToStream(IBitmapImageSource bitmapImageSource)

{

MemoryStream stream = new MemoryStream();

BitmapEncoder encoder = new PngBitmapEncoder(); // Or any other suitable encoder like JpegBitmapEncoder

BitmapSource bitmapSource = BitmapImageSourceToBitmapSource(bitmapImageSource);

encoder.Frames.Add(BitmapFrame.Create(bitmapSource));

encoder.Save(stream);

stream.Seek(0, SeekOrigin.Begin);

return stream;

}

public BitmapSource BitmapImageSourceToBitmapSource(

IBitmapImageSource bitmapImageSource)

{

if (bitmapImageSource == null)

{

return null;

}

int width = bitmapImageSource.Width;

int height = bitmapImageSource.Height;

PixelFormat format = PixelFormats.Bgr32;

int bpp = format.BitsPerPixel;

int stride = ((width * bpp) + 7) / 8;

byte[] pixels = bitmapImageSource.GetPixels();

return BitmapSource.Create(

width, height, 96, 96,

format, null, pixels, stride);

}

public void CancelRender()

=> _callbackHandler?.OnRenderActionRequested(RenderAction_e.Cancel);

public void CancelAndSaveRender()

=> _callbackHandler?.OnRenderActionRequested(RenderAction_e.CancelAndSave);

private void RequestPreview(object sender, ElapsedEventArgs e)

{

if (_previewRequestPending)

{

return;

}

float previewY = 300.0f;

float previewX = 400.0f;

if (RenderProgressDialog.ViewModel.AspectRatio >= previewX / previewY)

{

previewY = previewX / RenderProgressDialog.ViewModel.AspectRatio;

}

else

{

previewX = previewY / RenderProgressDialog.ViewModel.AspectRatio;

}

_callbackHandler?.OnPreviewRequested((int)previewX, (int)previewY);

_previewRequestPending = true;

}

public void **RendererPropertyChangedNotify**(RenderProperty_e renderProperty,

IRendererPropertiesStatus2 rendererPropertiesStatus)

{

if (renderProperty == RenderProperty_e.CurrentProgress)

{

RenderProgressDialog.ViewModel.RenderProgress = (double)(rendererPropertiesStatus.CurrentProgress * 100);

}

else if (renderProperty == RenderProperty_e.FramesRendered)

{

RenderProgressDialog.ViewModel.FramesRendered = rendererPropertiesStatus.FramesRendered;

}

else if (renderProperty == RenderProperty_e.ElapsedTime)

{

RenderProgressDialog.ViewModel.TimeSpan = rendererPropertiesStatus.ElapsedTime;

}

else if (renderProperty == RenderProperty_e.RenderJobStatus)

{

if (rendererPropertiesStatus.RenderJobStatus == RenderJobStatus_e.JobComplete ||

rendererPropertiesStatus.RenderJobStatus == RenderJobStatus_e.JobCancelled ||

rendererPropertiesStatus.RenderJobStatus == RenderJobStatus_e.JobAborted ||

rendererPropertiesStatus.RenderJobStatus == RenderJobStatus_e.JobFailed)

{

_requestPreviewTimer.Stop();

RenderProgressDialog.ViewModel.RenderCanceled -= CancelRender;

RenderProgressDialog.ViewModel.RenderCanceledAndSave -= CancelAndSaveRender;

}

else if (rendererPropertiesStatus.RenderJobStatus == RenderJobStatus_e.SaveComplete)

{

MessageBox.Show("Save Complete...");

_requestPreviewTimer.Start();

}

}

else if (renderProperty == RenderProperty_e.RendererPreviewComplete)

{

if (rendererPropertiesStatus.BitmapPreviewImageSource != null)

{

BitmapImage bitmapImage = new BitmapImage();

bitmapImage.BeginInit();

bitmapImage.CacheOption = BitmapCacheOption.OnLoad;

bitmapImage.StreamSource = BitmapSourceToStream(rendererPropertiesStatus.BitmapPreviewImageSource2);

bitmapImage.EndInit();

RenderProgressDialog.ViewModel.RenderedImage = bitmapImage;

_previewRequestPending = false;

}

}

}

public void **SetCallbackHandler**(IRenderCallbackHandler callbackHandler)

=> _callbackHandler = callbackHandler;

}

}

## Remarks

This interface extends [IRenderNotificationHander](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) by providing the ability to set a callback handler.

## See Also

[IRenderNotificationHandler2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2_members.html)
[SolidWorks.Visualize.Interfaces Namespace](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces_namespace.html)
