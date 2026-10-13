---
title: "GetHoleStandardsData Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetHoleStandardsData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetHoleStandardsData.html"
---

# GetHoleStandardsData Method (ISldWorks)

Gets the hole standards for the specified hole type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleStandardsData( _
   ByVal HoleTypeID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim HoleTypeID As System.Integer
Dim value As System.Object

value = instance.GetHoleStandardsData(HoleTypeID)
```

### C#

```csharp
System.object GetHoleStandardsData(
   System.int HoleTypeID
)
```

### C++/CLI

```cpp
System.Object^ GetHoleStandardsData(
   System.int HoleTypeID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleTypeID`: Hole Wizard hole type as defined in [swWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdGeneralHoleTypes_e.html)

### Return Value

[IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html); null if HoleTypeID is 5 (swWzdLegacy)

## VBA Syntax

See [SldWorks::GetHoleStandardsData](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetHoleStandardsData.html).

## Examples

[Get Hole Standards Data (VBA)](Get_Wizard_Hole_Standards_Data_Example_VB.htm)
[Get Hole Standards Data (C#)](Get_Wizard_Hole_Standards_Data_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
