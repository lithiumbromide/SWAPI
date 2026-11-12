---
title: "DeleteCustomInfo2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeleteCustomInfo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteCustomInfo2.html"
---

# DeleteCustomInfo2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteCustomInfo2( _
   ByVal Configuration As System.String, _
   ByVal FieldName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Configuration As System.String
Dim FieldName As System.String
Dim value As System.Boolean

value = instance.DeleteCustomInfo2(Configuration, FieldName)
```

### C#

```csharp
System.bool DeleteCustomInfo2(
   System.string Configuration,
   System.string FieldName
)
```

### C++/CLI

```cpp
System.bool DeleteCustomInfo2(
   System.String^ Configuration,
   System.String^ FieldName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`:
- `FieldName`:

## VBA Syntax

See [ModelDoc2::DeleteCustomInfo2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeleteCustomInfo2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
