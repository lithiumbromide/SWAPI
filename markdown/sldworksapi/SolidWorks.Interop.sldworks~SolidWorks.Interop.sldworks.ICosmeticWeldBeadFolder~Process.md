---
title: "Process Property (ICosmeticWeldBeadFolder)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFolder"
member: "Process"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder~Process.html"
---

# Process Property (ICosmeticWeldBeadFolder)

Gets or sets the weld process.

## Syntax

### Visual Basic (Declaration)

```vb
Property Process As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFolder
Dim value As System.String

instance.Process = value

value = instance.Process
```

### C#

```csharp
System.string Process {get; set;}
```

### C++/CLI

```cpp
property System.String^ Process {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weld process

## VBA Syntax

See [CosmeticWeldBeadFolder::Process](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFolder~Process.html).

## Examples

See [ICosmeticWeldBeadFolder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFolder.html) examples.

## See Also

[ICosmeticWeldBeadFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder.html)
[ICosmeticWeldBeadFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
