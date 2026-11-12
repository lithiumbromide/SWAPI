---
title: "IGetAll Method (ICustomPropertyManager)"
project: "SOLIDWORKS API Help"
interface: "ICustomPropertyManager"
member: "IGetAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll.html"
---

# IGetAll Method (ICustomPropertyManager)

Gets all of the custom properties for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetAll( _
   ByVal Count As System.Integer, _
   ByRef PropNames As System.String, _
   ByRef PropTypes As System.Integer, _
   ByRef PropValues As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomPropertyManager
Dim Count As System.Integer
Dim PropNames As System.String
Dim PropTypes As System.Integer
Dim PropValues As System.String

instance.IGetAll(Count, PropNames, PropTypes, PropValues)
```

### C#

```csharp
void IGetAll(
   System.int Count,
   out System.string PropNames,
   out System.int PropTypes,
   out System.string PropValues
)
```

### C++/CLI

```cpp
void IGetAll(
   System.int Count,
   [Out] System.String^ PropNames,
   [Out] System.int PropTypes,
   [Out] System.String^ PropValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of custom properties
- `PropNames`: Array of the names of custom properties
- `PropTypes`: Array of property types as defined in [swCustomInfoType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)
- `PropValues`: Array of values of custom properties

## VBA Syntax

See [CustomPropertyManager::IGetAll](ms-its:sldworksapivb6.chm::/sldworks~CustomPropertyManager~IGetAll.html).

## See Also

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.html)
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html)
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.html)
[ICustomPropertyManager::GetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
