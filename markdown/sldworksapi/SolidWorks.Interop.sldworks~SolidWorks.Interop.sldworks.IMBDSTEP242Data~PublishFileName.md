---
title: "PublishFileName Property (IMBDSTEP242Data)"
project: "SOLIDWORKS API Help"
interface: "IMBDSTEP242Data"
member: "PublishFileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data~PublishFileName.html"
---

# PublishFileName Property (IMBDSTEP242Data)

Gets or sets the path and file name to which to export this SOLIDWORKS MBD STEP 242 data.

## Syntax

### Visual Basic (Declaration)

```vb
Property PublishFileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMBDSTEP242Data
Dim value As System.String

instance.PublishFileName = value

value = instance.PublishFileName
```

### C#

```csharp
System.string PublishFileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ PublishFileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pathname of STEP 242 file (*.stp)

## VBA Syntax

See [MBDSTEP242Data::PublishFileName](ms-its:sldworksapivb6.chm::/sldworks~MBDSTEP242Data~PublishFileName.html).

## Examples

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html) examples.

## See Also

[IMBDSTEP242Data Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)
[IMBDSTEP242Data Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
