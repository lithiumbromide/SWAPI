---
title: "GetMagneticLinesCount Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetMagneticLinesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLinesCount.html"
---

# GetMagneticLinesCount Method (ISheet)

Gets the number of magnetic lines on this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMagneticLinesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Integer

value = instance.GetMagneticLinesCount()
```

### C#

```csharp
System.int GetMagneticLinesCount()
```

### C++/CLI

```cpp
System.int GetMagneticLinesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of magnetic lines on this sheet

## VBA Syntax

See [Sheet::GetMagneticLinesCount](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetMagneticLinesCount.html).

## Examples

[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::InsertMagneticLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.html)
[ISheet::GetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.html)
[ISheet::IGetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
