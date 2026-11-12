---
title: "GetFromToText Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetFromToText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText.html"
---

# GetFromToText Method (IGtol)

Gets the From-To text of this Gtol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFromToText( _
   ByRef FromText As System.String, _
   ByRef ToText As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FromText As System.String
Dim ToText As System.String
Dim value As System.Boolean

value = instance.GetFromToText(FromText, ToText)
```

### C#

```csharp
System.bool GetFromToText(
   out System.string FromText,
   out System.string ToText
)
```

### C++/CLI

```cpp
System.bool GetFromToText(
   [Out] System.String^ FromText,
   [Out] System.String^ ToText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromText`: From text label
- `ToText`: To text label

### Return Value

True if From-To text successfully retrieved, false if not

## VBA Syntax

See [Gtol::GetFromToText](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetFromToText.html).

## Examples

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.html) examples.

## Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

Before calling this method, use [IGtol::GetFromTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromTo.html) to determine whether the From-To symbol is present.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::SetFromToText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
