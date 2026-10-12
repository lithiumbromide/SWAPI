---
title: "ICreateEllipticalArcByCenter Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreateEllipticalArcByCenter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateEllipticalArcByCenter.html"
---

# ICreateEllipticalArcByCenter Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreateEllipticalArcByCenter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateEllipticalArcByCenter( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double
Dim Start As System.Double
Dim End As System.Double

instance.ICreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

### C#

```csharp
void ICreateEllipticalArcByCenter(
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor,
   ref System.double Start,
   ref System.double End
)
```

### C++/CLI

```cpp
void ICreateEllipticalArcByCenter(
   System.double% Center,
   System.double% Major,
   System.double% Minor,
   System.double% Start,
   System.double% End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`:
- `Major`:
- `Minor`:
- `Start`:
- `End`:

## VBA Syntax

See [ModelDoc::ICreateEllipticalArcByCenter](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreateEllipticalArcByCenter.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
