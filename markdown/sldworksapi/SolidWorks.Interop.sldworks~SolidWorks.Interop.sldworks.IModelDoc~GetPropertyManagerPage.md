---
title: "GetPropertyManagerPage Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetPropertyManagerPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetPropertyManagerPage.html"
---

# GetPropertyManagerPage Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetPropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetPropertyManagerPage.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyManagerPage( _
   ByVal DialogId As System.Integer, _
   ByVal Title As System.String, _
   ByVal Handler As System.Object _
) As PropertyManagerPage
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim DialogId As System.Integer
Dim Title As System.String
Dim Handler As System.Object
Dim value As PropertyManagerPage

value = instance.GetPropertyManagerPage(DialogId, Title, Handler)
```

### C#

```csharp
PropertyManagerPage GetPropertyManagerPage(
   System.int DialogId,
   System.string Title,
   System.object Handler
)
```

### C++/CLI

```cpp
PropertyManagerPage^ GetPropertyManagerPage(
   System.int DialogId,
   System.String^ Title,
   System.Object^ Handler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DialogId`:
- `Title`:
- `Handler`:

## VBA Syntax

See [ModelDoc::GetPropertyManagerPage](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetPropertyManagerPage.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
