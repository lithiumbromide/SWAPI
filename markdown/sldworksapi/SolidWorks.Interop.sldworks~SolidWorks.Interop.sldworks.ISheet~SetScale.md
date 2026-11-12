---
title: "SetScale Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetScale.html"
---

# SetScale Method (ISheet)

Sets the scale for this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetScale( _
   ByVal Numerator As System.Double, _
   ByVal Denominator As System.Double, _
   ByVal ScaleAnnoPosition As System.Boolean, _
   ByVal ScaleAnnoTextHeight As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Numerator As System.Double
Dim Denominator As System.Double
Dim ScaleAnnoPosition As System.Boolean
Dim ScaleAnnoTextHeight As System.Boolean
Dim value As System.Boolean

value = instance.SetScale(Numerator, Denominator, ScaleAnnoPosition, ScaleAnnoTextHeight)
```

### C#

```csharp
System.bool SetScale(
   System.double Numerator,
   System.double Denominator,
   System.bool ScaleAnnoPosition,
   System.bool ScaleAnnoTextHeight
)
```

### C++/CLI

```cpp
System.bool SetScale(
   System.double Numerator,
   System.double Denominator,
   System.bool ScaleAnnoPosition,
   System.bool ScaleAnnoTextHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Numerator`: First value in the scale ratio (n : n)
- `Denominator`: Second value in the scale ratio (n : n)
- `ScaleAnnoPosition`: True if the position of the annotations is scaled, false if not
- `ScaleAnnoTextHeight`: True if the text height of the annotations is scaled, false if not

### Return Value

True if the scale is set, false if not

## VBA Syntax

See [Sheet::SetScale](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SetScale.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

You can get the two scale values from the sheet by using [ISheet::GetProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetProperties.html) or [ISheet::IGetProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~IGetProperties.html).

You can also set the two scale values by using [IDrawingDoc::SetupSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~SetupSheet4.html) or [ISheet::SetProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SetProperties.html). However, you cannot specify the scaling of the position or text height of the annotations. Instead, both of these methods automatically scale the position of the annotations but do not scale the text height of the annotations when the drawing is changed.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.html)

## Availability

SOLIDWORKS 2001Plus SP5, Revision Number 10.5
