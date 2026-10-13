---
title: "Add2 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Add2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add2.html"
---

# Add2 Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Add3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Add3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Add2( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim value As System.Integer

value = instance.Add2(FieldName, FieldType, FieldValue)
```

### C#

```csharp
System.int Add2(
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.int Add2(
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of custom property
- `FieldType`: Type of custom property as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `FieldValue`: Value of custom property

### Return Value

- 1 if custom property is added
- 0 if custom property is not added
- -1 if the custom property already exists

## VBA Syntax

See [CustomPropertyManager::Add2](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Add2.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomerPropertyManager::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
