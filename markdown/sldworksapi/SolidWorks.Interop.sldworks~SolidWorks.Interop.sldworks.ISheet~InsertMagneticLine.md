---
title: "InsertMagneticLine Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "InsertMagneticLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.html"
---

# InsertMagneticLine Method (ISheet)

Inserts a magnetic line at the specified start and end points on this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMagneticLine( _
   ByVal StartPoint As MathPoint, _
   ByVal EndPoint As MathPoint _
) As MagneticLine
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim StartPoint As MathPoint
Dim EndPoint As MathPoint
Dim value As MagneticLine

value = instance.InsertMagneticLine(StartPoint, EndPoint)
```

### C#

```csharp
MagneticLine InsertMagneticLine(
   MathPoint StartPoint,
   MathPoint EndPoint
)
```

### C++/CLI

```cpp
MagneticLine^ InsertMagneticLine(
   MathPoint^ StartPoint,
   MathPoint^ EndPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartPoint`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)
- `EndPoint`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

### Return Value

[IMagneticLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine.html)

## VBA Syntax

See [Sheet::InsertMagneticLine](ms-its:sldworksapivb6.chm::/sldworks~Sheet~InsertMagneticLine.html).

## Examples

[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.html)
[ISheet::GetMagneticLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLinesCount.html)
[ISheet::IGetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
