---
title: "GetType2 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetType2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.html"
---

# GetType2 Method (ICustomPropertyManager)

Gets the type of the specified custom property for a configuration or model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType2( _
   ByVal FieldName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.Integer

value = instance.GetType2(FieldName)
```

### C#

```csharp
System.int GetType2(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.int GetType2(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property whose type to get

### Return Value

Type of custom property as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

## VBA Syntax

See [CustomPropertyManager::GetType2](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetType2.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

## Remarks

This method is not currently implemented for features.

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html)
[ICustomPropertyManager::Get5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
