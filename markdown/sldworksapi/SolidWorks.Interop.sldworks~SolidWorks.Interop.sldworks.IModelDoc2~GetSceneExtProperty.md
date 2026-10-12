---
title: "GetSceneExtProperty Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetSceneExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneExtProperty.html"
---

# GetSceneExtProperty Method (IModelDoc2)

Gets a float, string, or integer value stored for the scene.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSceneExtProperty( _
   ByVal PropertyId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PropertyId As System.Integer
Dim value As System.Object

value = instance.GetSceneExtProperty(PropertyId)
```

### C#

```csharp
System.object GetSceneExtProperty(
   System.int PropertyId
)
```

### C++/CLI

```cpp
System.Object^ GetSceneExtProperty(
   System.int PropertyId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyId`: ID of the property extension

### Return Value

Value stored for the scene extension property

## VBA Syntax

See [ModelDoc2::GetSceneExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetSceneExtProperty.html).

## Remarks

The type returned is based on the how the data was placed. See [IModelDoc2::AddSceneExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddSceneExtProperty.html) for deatails.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ResetSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetSceneExtProperty.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
