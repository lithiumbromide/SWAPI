---
title: "IGetMagneticLines Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IGetMagneticLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetMagneticLines.html"
---

# IGetMagneticLines Method (ISheet)

Gets the magnetic lines on this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMagneticLines( _
   ByVal Count As System.Integer _
) As MagneticLine
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Count As System.Integer
Dim value As MagneticLine

value = instance.IGetMagneticLines(Count)
```

### C#

```csharp
MagneticLine IGetMagneticLines(
   System.int Count
)
```

### C++/CLI

```cpp
MagneticLine^ IGetMagneticLines(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of magnetic lines returned by this method

### Return Value

- In-process, unmanaged C++: Array of [IMagneticLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine.html)s

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

Before calling this method, call [ISheet::GetMagneticLinesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~GetMagneticLinesCount.html) to get the value for Count.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetMagneticLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetMagneticLines.html)
[ISheet::InsertMagneticLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertMagneticLine.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
