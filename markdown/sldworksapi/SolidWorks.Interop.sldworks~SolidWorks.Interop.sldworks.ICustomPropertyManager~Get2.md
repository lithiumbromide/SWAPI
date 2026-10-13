---
title: "Get2 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Get2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.html"
---

# Get2 Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Get3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Get3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Get2( _
   ByVal FieldName As System.String, _
   ByRef ValOut As System.String, _
   ByRef ReesolvedValOut As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim ValOut As System.String
Dim ReesolvedValOut As System.String

instance.Get2(FieldName, ValOut, ReesolvedValOut)
```

### C#

```csharp
void Get2(
   System.string FieldName,
   out System.string ValOut,
   out System.string ReesolvedValOut
)
```

### C++/CLI

```cpp
void Get2(
   System.String^ FieldName,
   [Out] System.String^ ValOut,
   [Out] System.String^ ReesolvedValOut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property
- `ValOut`: Value of the custom property
- `ReesolvedValOut`: Evaluated value of the custom property

## VBA Syntax

See [CustomPropertyManager::Get2](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Get2.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::GetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll.html)
[ICustomPropertyManager::IGetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll.html)
[ICustomPropertyManager::Set Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
