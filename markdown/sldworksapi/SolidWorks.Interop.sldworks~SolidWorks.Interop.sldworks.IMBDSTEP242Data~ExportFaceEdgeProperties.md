---
title: "ExportFaceEdgeProperties Property (IMBDSTEP242Data)"
project: "SOLIDWORKS API Help"
interface: "IMBDSTEP242Data"
member: "ExportFaceEdgeProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~ExportFaceEdgeProperties.html"
---

# ExportFaceEdgeProperties Property (IMBDSTEP242Data)

Gets or sets whether to export face and edge properties to the STEP 242 format.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExportFaceEdgeProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMBDSTEP242Data
Dim value As System.Boolean

instance.ExportFaceEdgeProperties = value

value = instance.ExportFaceEdgeProperties
```

### C#

```csharp
System.bool ExportFaceEdgeProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool ExportFaceEdgeProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to export face and edge properties, false to not

## VBA Syntax

See [MBDSTEP242Data::ExportFaceEdgeProperties](ms-its:sldworksapivb6.chm::/sldworks~MBDSTEP242Data~ExportFaceEdgeProperties.html).

## Examples

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html) examples.

## See Also

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
