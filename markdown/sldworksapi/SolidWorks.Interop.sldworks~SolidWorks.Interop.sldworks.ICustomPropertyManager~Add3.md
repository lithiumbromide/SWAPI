---
title: "Add3 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Add3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.html"
---

# Add3 Method (ICustomPropertyManager)

Adds a custom property to a configuration or model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Add3( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String, _
   ByVal OverwriteExisting As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim OverwriteExisting As System.Integer
Dim value As System.Integer

value = instance.Add3(FieldName, FieldType, FieldValue, OverwriteExisting)
```

### C#

```csharp
System.int Add3(
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue,
   System.int OverwriteExisting
)
```

### C++/CLI

```cpp
System.int Add3(
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue,
   System.int OverwriteExisting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of custom property
- `FieldType`: Type of custom property as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `FieldValue`: Value of custom property
- `OverwriteExisting`: Overwrite option as defined in [swCustomPropertyAddOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomPropertyAddOption_e.html)

### Return Value

Result code as defined in [swCustomInfoAddResult_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoAddResult_e.html)

## VBA Syntax

See [CustomPropertyManager::Add3](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Add3.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Delete2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2.html)
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
