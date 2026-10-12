---
title: "AddSceneExtProperty Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddSceneExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddSceneExtProperty.html"
---

# AddSceneExtProperty Method (IModelDoc2)

Stores a float, string, or integer value for a scene.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSceneExtProperty( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddSceneExtProperty(PropertyExtension)
```

### C#

```csharp
System.int AddSceneExtProperty(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddSceneExtProperty(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`: Value for the scene

### Return Value

Unique identifier returned to access the property extension in the future

## VBA Syntax

See [ModelDoc2::AddSceneExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddSceneExtProperty.html).

## Remarks

This scene extension property is stored on the model document, but is unique to the model's scene. To add the extension property, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the light source for future reference.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
