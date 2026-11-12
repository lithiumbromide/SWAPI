---
title: "GetAll Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll.html"
---

# GetAll Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::GetAll2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager~GetAll2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAll( _
   ByRef PropNames As System.Object, _
   ByRef PropTypes As System.Object, _
   ByRef PropValues As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim PropNames As System.Object
Dim PropTypes As System.Object
Dim PropValues As System.Object
Dim value As System.Integer

value = instance.GetAll(PropNames, PropTypes, PropValues)
```

### C#

```csharp
System.int GetAll(
   out System.object PropNames,
   out System.object PropTypes,
   out System.object PropValues
)
```

### C++/CLI

```cpp
System.int GetAll(
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropTypes,
   [Out] System.Object^ PropValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropNames`: Array of the names of custom properties
- `PropTypes`: Array of property types as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `PropValues`: Array of values of custom properties

### Return Value

Number of custom properties

## VBA Syntax

See [CustomPropertyManager::GetAll](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetAll.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.html)
[ICustomPropertyManager::IGetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll.html)
[ICustomPropertyManager::Set Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
