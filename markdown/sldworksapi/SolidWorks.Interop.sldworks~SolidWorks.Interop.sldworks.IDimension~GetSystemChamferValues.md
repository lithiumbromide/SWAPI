---
title: "GetSystemChamferValues Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetSystemChamferValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemChamferValues.html"
---

# GetSystemChamferValues Method (IDimension)

Gets the chamfer dimension values in system units.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSystemChamferValues( _
   ByRef Length As System.Double, _
   ByRef Angle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Length As System.Double
Dim Angle As System.Double
Dim value As System.Boolean

value = instance.GetSystemChamferValues(Length, Angle)
```

### C#

```csharp
System.bool GetSystemChamferValues(
   out System.double Length,
   out System.double Angle
)
```

### C++/CLI

```cpp
System.bool GetSystemChamferValues(
   [Out] System.double Length,
   [Out] System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Length`: Length of chamfer
- `Angle`: Angle of chamfer

### Return Value

True if the dimension is a chamfer dimension, false if not

## VBA Syntax

See [Dimension::GetSystemChamferValues](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetSystemChamferValues.html).

## Examples

[Get Chamfer Dimension (C#)](Get_Chamfer_Dimension_Example_CSharp.htm)
[Get Chamfer Dimension (VB.NET)](Get_Chamfer_Dimension_Example_VBNET.htm)
[Get Chamfer Dimension (VBA)](Get_Chamfer_Dimension_Example_VB.htm)

## Remarks

Unlike most other types of dimensions, the values returned for a chamfer dimension are not necessarily the values seen by the user in the displayed dimension text. The display dimension interprets these values and considers the type of chamfer display requested by the user and then creates an appropriate output string.

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDrawingDoc::AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.html)
[IDrawingDoc::IAddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddChamferDim.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14.1
