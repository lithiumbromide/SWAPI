---
title: "AddLightToScene Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddLightToScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightToScene.html"
---

# AddLightToScene Method (IModelDoc2)

Adds a light source to a scene.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLightToScene( _
   ByVal LpszNewValue As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim LpszNewValue As System.String
Dim value As System.Integer

value = instance.AddLightToScene(LpszNewValue)
```

### C#

```csharp
System.int AddLightToScene(
   System.string LpszNewValue
)
```

### C++/CLI

```cpp
System.int AddLightToScene(
   System.String^ LpszNewValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpszNewValue`: Name to use for the light

### Return Value

ID of the light

## VBA Syntax

See [ModelDoc2::AddLightToScene](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddLightToScene.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
