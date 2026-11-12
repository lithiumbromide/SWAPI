---
title: "Delete Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "Delete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete.html"
---

# Delete Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::Delete2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~Delete2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete( _
   ByVal FieldName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.Integer

value = instance.Delete(FieldName)
```

### C#

```csharp
System.int Delete(
   System.string FieldName
)
```

### C++/CLI

```cpp
System.int Delete(
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FieldName`: Name of the custom property to delete

### Return Value

0 if the custom property is deleted, 1 if not

## VBA Syntax

See [CustomPropertyManager::Delete](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~Delete.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomerPropertyManager::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
