---
title: "Getting Started"
project: "SOLIDWORKS Routing API Help"
interface: ""
member: ""
kind: "topic"
source: "routingapi/GettingStarted-routingapi.html"
---

# Getting Started

Writing a SOLIDWORKS Routing API application typically involves:

1. Adding a reference to SOLIDWORKS `version` Routing Type Library. Substitute the current SOLIDWORKS Design version number for `version`. For VBA and COM applications, add a reference to the type library, install_dir\SWRoutingLib.tlb. For .NET applications, add a reference to the interop assembly, `install_dir`**\api\redist\SOLIDWORKS.interop.SWRoutingLib.dll**.
2. Instantiating a SOLIDWORKS Design connection.
3. Loading the SOLIDWORKS Routing add-in, if it is not already loaded, using the SOLIDWORKS [ISldWorks::LoadAddIn](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadAddIn.html) method. The SOLIDWORKS Routing API DLL is sldrtadd.dll.
4. Opening a SOLIDWORKS Design assembly document that contains a route sub-assembly.
5. Using the SOLIDWORKS [IAssemblyDoc::GetRouteManager](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetRouteManager.html) method to get the SOLIDWORKS Routing API.
6. Getting the route.
7. Getting the cables and wires in the route.
8. Getting the route properties and editing the route.
