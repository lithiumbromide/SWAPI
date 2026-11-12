---
title: "GetAll2 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetAll2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll2.html"
---

# GetAll2 Method (ICustomPropertyManager)

Obsolete. Superseded by [ICustomPropertyManager::GetAll3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAll2( _
   ByRef PropNames As System.Object, _
   ByRef PropTypes As System.Object, _
   ByRef PropValues As System.Object, _
   ByRef Resolved As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim PropNames As System.Object
Dim PropTypes As System.Object
Dim PropValues As System.Object
Dim Resolved As System.Object
Dim value As System.Integer

value = instance.GetAll2(PropNames, PropTypes, PropValues, Resolved)
```

### C#

```csharp
System.int GetAll2(
   out System.object PropNames,
   out System.object PropTypes,
   out System.object PropValues,
   out System.object Resolved
)
```

### C++/CLI

```cpp
System.int GetAll2(
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropTypes,
   [Out] System.Object^ PropValues,
   [Out] System.Object^ Resolved
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropNames`: Array of the names of custom properties retrieved
- `PropTypes`: Array of types of PropNames as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `PropValues`: Array of evaluated values of PropNames
- `Resolved`: Array of evaluation statuses of PropNames as defined in [swCustomInfoGetResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoGetResult_e.html)

### Return Value

Number of custom properties retrieved

## VBA Syntax

See [CustomPropertyManager::GetAll2](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetAll2.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get5.html)
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html)
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html)
[ICustomPropertyManager::IGetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetNames.html)
[ICustomPropertyManager::GetType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
