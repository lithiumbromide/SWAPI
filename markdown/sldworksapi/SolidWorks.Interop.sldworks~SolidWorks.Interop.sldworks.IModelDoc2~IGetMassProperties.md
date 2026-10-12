---
title: "IGetMassProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetMassProperties.html"
---

# IGetMassProperties Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::IGetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetMassProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties( _
   ByRef MPropsData As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::IGetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetMassProperties.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
