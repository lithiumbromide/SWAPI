---
title: "BackgroundProcessingOption Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "BackgroundProcessingOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BackgroundProcessingOption.html"
---

# BackgroundProcessingOption Property (IDrawingDoc)

Gets or sets the background processing option for this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundProcessingOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Integer

instance.BackgroundProcessingOption = value

value = instance.BackgroundProcessingOption
```

### C#

```csharp
System.int BackgroundProcessingOption {get; set;}
```

### C++/CLI

```cpp
property System.int BackgroundProcessingOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Background processing option as defined in [swBackgroundProcessOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html) (see **Remarks**)

## VBA Syntax

See [DrawingDoc::BackgroundProcessingOption](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~BackgroundProcessingOption.html).

## Examples

[Fire Notifications for Background Processing Events (VBA)](Fire_Notification_for_Background_Processing_Events_Example_VB.htm)
[Fire Notifications for Background Processing Events (VB.NET)](Fire_Notification_for_Background_Processing_Events_Example_VBNET.htm)
[Fire Notifications for Background Processing Events (C#)](Fire_Notification_for_Background_Processing_Events_Example_CSharp.htm)

## Remarks

SOLIDWORKS recommends that you only use this property with [ISldWorks::IsBackgroundProcessingCompleted](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.html) and [ISldWorks::EnableBackgroundProcessing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.html) when you can quickly open a drawing document via the user interface, but that same drawing takes significantly more time to open programmatically.

To more efficiently and programmatically open a drawing document that requires a lot of CPU time and no user input:

1. Set ISldWorks::EnableBackgroundProcessing to true.
2. Use [ISldWorks Event BackgroundProcessingStartNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_BackgroundProcessingStartNotifyEventHandler.html) to handle the background processing start event.
3. Open the drawing document by calling either [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) or [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html).
4. Set IDrawingDoc::BackgroundProcessingOption to [swBackgroundProcessOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBackgroundProcessOption_e.html).swBackgroundProcessing_DeferToApplication.
5. Call ISldWorks::IsBackgroundProcessingCompleted repeatedly, which polls the status of the open operation
6. Use [ISldWorks Event BackgroundProcessingEndNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_BackgroundProcessingEndNotifyEventHandler.html) to handle the background processing end event.
7. When the open operation is finished, set ISldWorks::EnableBackgroundProcessing to false.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
