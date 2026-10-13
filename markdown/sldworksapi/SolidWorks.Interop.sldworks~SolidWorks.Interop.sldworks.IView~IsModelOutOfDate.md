---
title: "IsModelOutOfDate Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsModelOutOfDate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate.html"
---

# IsModelOutOfDate Method (IView)

Gets whether the model in this drawing view is up-to-date with the current model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsModelOutOfDate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsModelOutOfDate()
```

### C#

```csharp
System.bool IsModelOutOfDate()
```

### C++/CLI

```cpp
System.bool IsModelOutOfDate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the view is out of date, false if not

## VBA Syntax

See [View::IsModelOutOfDate](ms-its:sldworksapivb6.chm::/sldworks~View~IsModelOutOfDate.html).

## Remarks

A model can be out-of-date in a Detached drawing where the model is not loaded, if any of the views in any of the sheets in the drawing refers to a model that has been modified and saved to disk since this drawing was last saved. This situation is flagged upon opening a document as well.

If you are using [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) with the silent option enabled, this warning is returned via the Warnings argument by value swFileLoadWarning_ModelOutOfDate. If you print this drawing and have the swRapidDraftPrintOutOfSynchWaterMark user preference enabled (see [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html)), then the printout will indicate this drawing as being out-of-synch.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsModelLoaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded.html)
[IView::LoadModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LoadModel.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
