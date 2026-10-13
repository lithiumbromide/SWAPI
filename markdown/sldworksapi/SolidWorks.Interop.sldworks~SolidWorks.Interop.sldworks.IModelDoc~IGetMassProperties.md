---
title: "IGetMassProperties Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetMassProperties.html"
---

# IGetMassProperties Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetMassProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties( _
   ByRef MPropsData As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim MPropsData As System.Double
Dim value As System.Boolean

value = instance.IGetMassProperties(MPropsData)
```

### C#

```csharp
System.bool IGetMassProperties(
   ref System.double MPropsData
)
```

### C++/CLI

```cpp
System.bool IGetMassProperties(
   System.double% MPropsData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MPropsData`:

## VBA Syntax

See [ModelDoc::IGetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetMassProperties.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
