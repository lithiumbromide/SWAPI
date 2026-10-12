---
title: "GetNames Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html"
---

# GetNames Method (ICustomPropertyManager)

Gets the names of the custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim value As System.Object

value = instance.GetNames()
```

### C#

```csharp
System.object GetNames()
```

### C++/CLI

```cpp
System.Object^ GetNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Names of the custom properties

## VBA Syntax

See [CustomPropertyManager::GetNames](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetNames.html).

## Examples

[Add and Get Custom Properties (VBA)](Add_and_Get_Custom_Properties_Example_VB.htm)
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::IGetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetNames.html)
[ICustomPropertyManager::Get5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.html)
[ICustomPropertyManager::GetAll2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll2.html)
[ICustomPropertyManager::IsCustomPropertyEditable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IsCustomPropertyEditable.html)

## Availability

SOLIDWORKS 2004 FCS, Revision number 12.0
