---
title: "GetText Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetText.html"
---

# GetText Method (IGtol)

Gets the specified text part of this GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal WhichText As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim WhichText As System.Integer
Dim value As System.String

value = instance.GetText(WhichText)
```

### C#

```csharp
System.string GetText(
   System.int WhichText
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int WhichText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Text part to get as defined in [swGTolTextParts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGTolTextParts_e.html)

### Return Value

Text part

## VBA Syntax

See [Gtol::GetText](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetText.html).

## Examples

See **Set Text in Datum Tags and GTols** examples in [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetText.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
