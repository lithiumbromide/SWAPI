---
title: "GetUserUnit Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html"
---

# GetUserUnit Method (IModelDoc2)

Gets this document's units settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserUnit( _
   ByVal UnitType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UnitType As System.Integer
Dim value As System.Object

value = instance.GetUserUnit(UnitType)
```

### C#

```csharp
System.object GetUserUnit(
   System.int UnitType
)
```

### C++/CLI

```cpp
System.Object^ GetUserUnit(
   System.int UnitType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitType`: Document unit type as defined in [swUserUnitsType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

### Return Value

[IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)

## VBA Syntax

See [ModelDoc2::GetUserUnit](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetUserUnit.html).

## Examples

[Get and Set Document Units (VBA)](Get_and_Set_User_Units_Example_VB.htm)
[Get and Set Document Units (VB.NET)](Get_and_Set_User_Units_Example_VBNET.htm)
[Get and Set Document Units (C#)](Get_and_Set_User_Units_Example_CSharp.htm)

## Remarks

The properties of IUserUnit are read only. Set them using the IModelDocExtension::SetUserPreference* methods.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.html)
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.html)
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.html)
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.html)
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html)
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.html)
[IModelDoc2::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.html)
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.html)
[ISldWorks::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
