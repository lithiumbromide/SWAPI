---
title: "SetIndependentViewPort Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "SetIndependentViewPort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetIndependentViewPort.html"
---

# SetIndependentViewPort Method (IMBD3DPdfData)

Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetIndependentViewPort( _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.SetIndependentViewPort(ViewName)
```

### C#

```csharp
System.bool SetIndependentViewPort(
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool SetIndependentViewPort(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the view (e.g., "Top View" or "*Top")

### Return Value

True if the specified view is set for an independent viewport for the SOLIDWORKS MBD 3D PDF, false if not (see **Remarks**)

## VBA Syntax

See [MBD3DPdfData::SetIndependentViewPort](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~SetIndependentViewPort.html).

## Examples

[Set Independent Viewport for MBD 3D PDF (C#)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_CSharp.htm)
[Set Independent Viewport for MBD 3D PDF (VB.NET)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_VBNET.htm)
[Set Independent Viewport for MBD 3D PDF (VBA)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_VB.htm)

## Remarks

The [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) for the SOLIDWORKS MBD 3D PDF must contain an independent viewport. See the examples for instructions on how to add an independent viewport to a theme and how to set a view for that independent viewport.

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
