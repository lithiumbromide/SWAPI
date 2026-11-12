---
title: "Set Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Set"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set.html"
---

# Set Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Set2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Set2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Set( _
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

value = instance.Set(FieldName, FieldValue)
```

### C#

```csharp
System.int Set(
   System.string FieldName,
   System.string FieldValue
)
```

### C++/CLI

```cpp
System.int Set(
   System.String^ FieldName,
   System.String^ FieldValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the existing custom property
- `FieldValue`: Value for the existing custom property

### Return Value

- 0 if the value for the existing custom property is set
- 1 if the value for the existing custom property is not set
- -1 if the custom property does not exist

## VBA Syntax

See [CustomPropertyManager::Set](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Set.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
