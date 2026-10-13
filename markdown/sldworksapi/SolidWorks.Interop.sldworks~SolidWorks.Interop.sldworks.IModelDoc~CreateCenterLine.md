---
title: "CreateCenterLine Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCenterLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCenterLine.html"
---

# CreateCenterLine Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCenterLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCenterLine( _
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

value = instance.CreateCenterLine(P1, P2)
```

### C#

```csharp
System.bool CreateCenterLine(
   System.object P1,
   System.object P2
)
```

### C++/CLI

```cpp
System.bool CreateCenterLine(
   System.Object^ P1,
   System.Object^ P2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1`:
- `P2`:

## VBA Syntax

See [ModelDoc::CreateCenterLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCenterLine.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
