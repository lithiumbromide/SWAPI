---
title: "IsolateChangedDimensions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IsolateChangedDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IsolateChangedDimensions.html"
---

# IsolateChangedDimensions Method (IDrawingDoc)

Isolates changed dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IsolateChangedDimensions()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.IsolateChangedDimensions()
```

### C#

```csharp
void IsolateChangedDimensions()
```

### C++/CLI

```cpp
void IsolateChangedDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::IsolateChangedDimensions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IsolateChangedDimensions.html).

## Examples

[Isolate Changed Dimension (C#)](Isolate_Changed_Dimension_Example_CSharp.htm)
[Isolate Changed Dimension (VB.NET)](Isolate_Changed_Dimension_Example_VBNET.htm)
[Isolate Changed Dimension (VBA)](Isolate_Changed_Dimension_Example_VB.htm)

## Remarks

This method only works with drawings saved in SOLIDWORKS 2012 and later.

To isolate changed dimensions:

1. Call [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) and set its UserPreferenceValue argument to swUserPreferenceToggle_e.swUseChangedDimensions and its OnFlag argument to true.
2. Call IDrawingDoc::IsolateChangedDimensions.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision 20.0
