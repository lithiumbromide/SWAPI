---
title: "GetAll3 Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "GetAll3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll3.html"
---

# GetAll3 Method (ICustomPropertyManager)

Gets all of the custom properties for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAll3( _
   ByRef PropNames As System.Object, _
   ByRef PropTypes As System.Object, _
   ByRef PropValues As System.Object, _
   ByRef Resolved As System.Object, _
   ByRef PropLink As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim PropNames As System.Object
Dim PropTypes As System.Object
Dim PropValues As System.Object
Dim Resolved As System.Object
Dim PropLink As System.Object
Dim value As System.Integer

value = instance.GetAll3(PropNames, PropTypes, PropValues, Resolved, PropLink)
```

### C#

```csharp
System.int GetAll3(
   out System.object PropNames,
   out System.object PropTypes,
   out System.object PropValues,
   out System.object Resolved,
   out System.object PropLink
)
```

### C++/CLI

```cpp
System.int GetAll3(
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropTypes,
   [Out] System.Object^ PropValues,
   [Out] System.Object^ Resolved,
   [Out] System.Object^ PropLink
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropNames`: Array of the names of custom properties retrieved
- `PropTypes`: Array of types of PropNames as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `PropValues`: Array of evaluated values of PropNames
- `Resolved`: Array of evaluation statuses of PropNames as defined in [swCustomInfoGetResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoGetResult_e.html)
- `PropLink`: Array of integers indicating whether PropNames are linked to their parent parts:

  1 = link

  0 = no link

### Return Value

Number of custom properties returned

## VBA Syntax

See [CustomPropertyManager::GetAll3](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~GetAll3.html).

## Examples

See the **Get Custom Properties for Configuration** examples in [ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.html)
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html)
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html)
[ICustomPropertyManager::GetType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
