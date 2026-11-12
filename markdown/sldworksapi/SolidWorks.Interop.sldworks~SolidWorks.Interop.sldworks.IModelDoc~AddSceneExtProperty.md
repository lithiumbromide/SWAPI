---
title: "AddSceneExtProperty Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddSceneExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddSceneExtProperty.html"
---

# AddSceneExtProperty Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddSceneExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddSceneExtProperty.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSceneExtProperty( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
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

- `PropertyExtension`:

## VBA Syntax

See [ModelDoc::AddSceneExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddSceneExtProperty.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
