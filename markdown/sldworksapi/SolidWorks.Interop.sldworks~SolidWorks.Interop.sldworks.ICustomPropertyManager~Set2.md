---
title: "Set2 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Set2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html"
---

# Set2 Method (ICustomPropertyManager)

Sets the value for the specified custom property.

## Syntax

### Visual Basic (Declaration)

```vb
Function Set2( _
   ByVal FieldName As System.String, _
   ByVal FieldValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldValue As System.String
Dim value As System.Integer

value = instance.Set2(FieldName, FieldValue)
```

### C#

```csharp
System.int Set2(
   System.string FieldName,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.int Set2(
   System.String^ FieldName,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the existing custom property
- `FieldValue`: Value for the existing custom property

### Return Value

Result code as defined in [swCustomInfoSetResult_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoSetResult_e.html)

## VBA Syntax

See [CustomPropertyManager::Set2](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Set2.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.html)
[ICustomPropertyManager::GetAll2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll2.html)
[ICustomPropertyManager::Add3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
