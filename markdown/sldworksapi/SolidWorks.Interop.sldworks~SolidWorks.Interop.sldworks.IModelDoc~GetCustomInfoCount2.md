---
title: "GetCustomInfoCount2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetCustomInfoCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetCustomInfoCount2.html"
---

# GetCustomInfoCount2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetCustomInfoCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetCustomInfoCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomInfoCount2( _
   ByVal Configuration As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Configuration As System.String
Dim value As System.Integer

value = instance.GetCustomInfoCount2(Configuration)
```

### C#

```csharp
System.int GetCustomInfoCount2(
   System.string Configuration
)
```

### C++/CLI

```cpp
System.int GetCustomInfoCount2(
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:

## VBA Syntax

See [ModelDoc::GetCustomInfoCount2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetCustomInfoCount2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
