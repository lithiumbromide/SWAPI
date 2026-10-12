---
title: "AddLightSourceExtProperty Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddLightSourceExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightSourceExtProperty.html"
---

# AddLightSourceExtProperty Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddLightSourceExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddLightSourceExtProperty(ID, PropertyExtension)
```

### C#

```csharp
System.int AddLightSourceExtProperty(
   System.int ID,
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddLightSourceExtProperty(
   System.int ID,
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:
- `PropertyExtension`:

## VBA Syntax

See [ModelDoc::AddLightSourceExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddLightSourceExtProperty.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
