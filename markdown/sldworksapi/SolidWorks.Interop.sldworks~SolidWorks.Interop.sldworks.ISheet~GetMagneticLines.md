---
title: "GetMagneticLines Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetMagneticLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.html"
---

# GetMagneticLines Method (ISheet)

Gets the magnetic lines on this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMagneticLines() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Object

value = instance.GetMagneticLines()
```

### C#

```csharp
System.object GetMagneticLines()
```

### C++/CLI

```cpp
System.Object^ GetMagneticLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IMagneticLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine.html)s

## VBA Syntax

See [Sheet::GetMagneticLines](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetMagneticLines.html).

## Remarks

Call [ISheet::GetMagneticLinesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetMagneticLinesCount.html) to get the number of magnetic lines returned by this method.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::IGetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.html)
[ISheet::InsertMagneticLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
