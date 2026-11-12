---
title: "IsCustomPropertyEditable Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "IsCustomPropertyEditable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IsCustomPropertyEditable.html"
---

# IsCustomPropertyEditable Method (ICustomPropertyManager)

Gets whether the specified custom property is editable in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCustomPropertyEditable( _
   ByVal PropertyName As System.String, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim PropertyName As System.String
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.IsCustomPropertyEditable(PropertyName, ConfigurationName)
```

### C#

```csharp
System.bool IsCustomPropertyEditable(
   System.string PropertyName,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool IsCustomPropertyEditable(
   System.String^ PropertyName,
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyName`: Custom property name
- `ConfigurationName`: Configuration name

### Return Value

True if the custom property is editable, false if not

## VBA Syntax

See [CustomPropertyManager::IsCustomPropertyEditable](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~IsCustomPropertyEditable.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

## Remarks

Use [ICustomPropertyManager::GetNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html) to populate PropertyName.

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
