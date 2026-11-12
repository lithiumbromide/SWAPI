---
title: "ICreateEllipse Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreateEllipse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse.html"
---

# ICreateEllipse Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateEllipse2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateEllipse( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double

instance.ICreateEllipse(Center, Major, Minor)
```

### C#

```csharp
void ICreateEllipse(
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor
)
```

### C++/CLI

```cpp
void ICreateEllipse(
   System.double% Center,
   System.double% Major,
   System.double% Minor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Major`:
- `Minor`:

## VBA Syntax

See [ModelDoc2::ICreateEllipse](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreateEllipse.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
