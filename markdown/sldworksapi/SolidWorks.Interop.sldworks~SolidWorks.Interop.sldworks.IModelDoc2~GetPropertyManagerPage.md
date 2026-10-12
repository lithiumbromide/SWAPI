---
title: "GetPropertyManagerPage Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetPropertyManagerPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyManagerPage.html"
---

# GetPropertyManagerPage Method (IModelDoc2)

Obsolete. Superseded by [ISldWorks::CreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) and [ISldWorks::ICreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::GetPropertyManagerPage](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetPropertyManagerPage.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
