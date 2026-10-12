---
title: "IGetCustomInfoNames2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetCustomInfoNames2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetCustomInfoNames2.html"
---

# IGetCustomInfoNames2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCustomInfoNames2( _
   ByVal Configuration As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Configuration As System.String
Dim value As System.String

value = instance.IGetCustomInfoNames2(Configuration)
```

### C#

```csharp
System.string IGetCustomInfoNames2(
   System.string Configuration
)
```

### C++/CLI

```cpp
System.String^ IGetCustomInfoNames2(
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:

## VBA Syntax

See [ModelDoc2::IGetCustomInfoNames2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetCustomInfoNames2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
