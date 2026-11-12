---
title: "GetFromTo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFromTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromTo.html"
---

# GetFromTo Method (IGtol)

Gets whether the From-To symbol is present in this Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFromTo() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Boolean

value = instance.GetFromTo()
```

### C#

```csharp
System.bool GetFromTo()
```

### C++/CLI

```cpp
System.bool GetFromTo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if From-To symbol is present, false if not

## VBA Syntax

See [Gtol::GetFromTo](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFromTo.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

If this method returns true, then call [IGtol::GetFromToText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText.html) and [IGtol::SetFromToText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText.html) to retrieve and set the From-To labels for this Gtol.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
