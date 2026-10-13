---
title: "CreateLine Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateLine.html"
---

# CreateLine Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLine( _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim P1 As System.Object
Dim P2 As System.Object
Dim value As System.Boolean

value = instance.CreateLine(P1, P2)
```

### C#

```csharp
System.bool CreateLine(
   System.object P1,
   System.object P2
)
```

### C++/CLI

```cpp
System.bool CreateLine(
   System.Object^ P1,
   System.Object^ P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:

## VBA Syntax

See [ModelDoc::CreateLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateLine.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
