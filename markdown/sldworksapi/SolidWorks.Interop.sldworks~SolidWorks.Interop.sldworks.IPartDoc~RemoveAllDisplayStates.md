---
title: "RemoveAllDisplayStates Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "RemoveAllDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~RemoveAllDisplayStates.html"
---

# RemoveAllDisplayStates Method (IPartDoc)

Removes all display states and appearances from this part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllDisplayStates() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Boolean

value = instance.RemoveAllDisplayStates()
```

### C#

```csharp
System.bool RemoveAllDisplayStates()
```

### C++/CLI

```cpp
System.bool RemoveAllDisplayStates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [PartDoc::RemoveAllDisplayStates](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~RemoveAllDisplayStates.html).

## Examples

[Clear Display States (VBA)](Clear_Display_States_Example_VB.htm)
[Clear Display States (VB.NET)](Clear_Display_States_Example_VBNET.htm)
[Clear Display States (C#)](Clear_Display_States_Example_CSharp.htm)

## Remarks

Call this method to:

- Remove all appearances from all configurations of this part.
- Remove all display states except the active display state.
- Un-link display states from configurations.
- Show all hidden features.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2011 SP4, Revision Number 19.4
