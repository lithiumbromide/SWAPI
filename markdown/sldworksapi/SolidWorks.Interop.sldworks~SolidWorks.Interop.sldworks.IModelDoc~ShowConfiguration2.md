---
title: "ShowConfiguration2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ShowConfiguration2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ShowConfiguration2.html"
---

# ShowConfiguration2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ShowConfiguration2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowConfiguration2( _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.ShowConfiguration2(ConfigurationName)
```

### C#

```csharp
System.bool ShowConfiguration2(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool ShowConfiguration2(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`:

## VBA Syntax

See [ModelDoc::ShowConfiguration2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ShowConfiguration2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
