---
title: "Getting Started"
project: "FeatureWorks API Help"
interface: ""
member: ""
kind: "topic"
source: "fworksapi/GettingStarted-fworksapi.html"
---

# Getting Started

Writing a FeatureWorks API application typically involves:

1. Instantiating a SOLIDWORKS Design connection.
2. Getting the FeatureWorks object.
3. Recognizing imported features either automatically or interactively ([IFeatureWorksApp::RecognizeFeatureAutomatic](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.IFeatureWorksApp~RecognizeFeatureAutomatic.html), [IFeatureWorksApp::RecognizeFeatureInteractive](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.IFeatureWorksApp~RecognizeFeatureInteractive.html)).

  You can call these methods multiple times to recognize various features.
4. Creating all of the recognized features ([IFeatureWorksApp::CreateFeatures](SOLIDWORKS.Interop.fworks~SOLIDWORKS.Interop.fworks.IFeatureWorksApp~CreateFeatures.html)).

  The recognized features are displayed in the FeatureManager design tree.

The FeatureWorks DLLs must be loaded before calling the FeatureWorks API.

FeatureWorks operations such as combining, re-recognizing features, and recognizing patterns are not supported. The FeatureWorks Local Feature Recognition and Recognize Similar options are also not supported.
