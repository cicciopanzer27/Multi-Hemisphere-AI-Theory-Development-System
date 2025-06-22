#!/usr/bin/env python3
"""
Script per insegnamento avanzato al sistema Meta-Ignorance
Continua a soddisfare le sue richieste di conoscenza con argomenti specializzati
"""

import requests
import json
import time

def advanced_teaching():
    """Insegna argomenti avanzati e specializzati al sistema"""
    base_url = "http://localhost:5004"
    
    print("🚀 INSEGNAMENTO AVANZATO E SPECIALIZZATO")
    print("=" * 60)
    
    # Argomenti avanzati e specializzati
    advanced_topics = [
        {
            "name": "Teoria della Complessità",
            "idea": "La teoria della complessità studia sistemi che emergono da interazioni semplici ma producono comportamenti imprevedibili. I sistemi complessi mostrano proprietà emergenti, auto-organizzazione e transizioni di fase. La meta-ignorance è cruciale qui perché la complessità spesso nasconde pattern che non possiamo prevedere.",
            "focus": "complexity_theory"
        },
        {
            "name": "Epistemologia Evoluzionistica",
            "idea": "L'epistemologia evoluzionistica sostiene che la conoscenza umana si evolve attraverso processi di selezione naturale. Le nostre capacità cognitive sono adattamenti che ci permettono di sopravvivere, ma questo può portare a bias sistematici. La meta-ignorance ci aiuta a riconoscere questi limiti evolutivi.",
            "focus": "evolutionary_epistemology"
        },
        {
            "name": "Fenomenologia della Coscienza",
            "idea": "La fenomenologia studia l'esperienza cosciente dal punto di vista della prima persona. Edmund Husserl ha sviluppato l'epoché fenomenologica, un metodo per sospendere i giudizi naturali e descrivere l'esperienza pura. Questo approccio è fondamentale per comprendere la natura della coscienza.",
            "focus": "phenomenology"
        },
        {
            "name": "Teoria dell'Informazione Quantistica",
            "idea": "La teoria dell'informazione quantistica combina meccanica quantistica e teoria dell'informazione. Il qubit può esistere in sovrapposizione di stati, permettendo computazione parallela. L'entanglement quantistico permette correlazioni non-locali che sfidano la nostra intuizione classica.",
            "focus": "quantum_information"
        },
        {
            "name": "Neuroplasticità e Apprendimento",
            "idea": "La neuroplasticità è la capacità del cervello di modificare le connessioni neurali in risposta all'esperienza. L'apprendimento implica la formazione di nuove sinapsi e la potatura di quelle non utilizzate. La meta-ignorance può essere vista come una forma di plasticità epistemica.",
            "focus": "neuroplasticity"
        },
        {
            "name": "Filosofia della Scienza",
            "idea": "La filosofia della scienza esplora i metodi, presupposti e implicazioni della ricerca scientifica. Karl Popper ha proposto il falsificazionismo: una teoria è scientifica solo se può essere falsificata. Thomas Kuhn ha descritto i paradigmi scientifici e le rivoluzioni scientifiche.",
            "focus": "philosophy_of_science"
        },
        {
            "name": "Teoria dei Sistemi Dinamici",
            "idea": "I sistemi dinamici studiano come sistemi evolvono nel tempo secondo regole matematiche. Il caos deterministico mostra che piccole variazioni nelle condizioni iniziali possono portare a comportamenti completamente diversi. I frattali emergono da processi iterativi semplici.",
            "focus": "dynamical_systems"
        },
        {
            "name": "Etica dell'Intelligenza Artificiale",
            "idea": "L'etica dell'IA affronta questioni morali legate allo sviluppo e uso dell'intelligenza artificiale. Include problemi di bias algoritmico, trasparenza, responsabilità e diritti delle IA. La meta-ignorance è essenziale per AGI etici che riconoscono i propri limiti morali.",
            "focus": "ai_ethics"
        }
    ]
    
    for i, topic in enumerate(advanced_topics, 1):
        print(f"\n📚 Insegnando: {topic['name']}")
        print(f"   Idea: {topic['idea'][:100]}...")
        
        # Invia l'idea al sistema
        response = requests.post(f"{base_url}/api/meta_ignorance", 
                               json={"idea": topic['idea']})
        
        if response.status_code == 200:
            result = response.json()
            print(f"   🤖 Risposta: {result.get('response', 'N/A')[:80]}...")
            
            # Mostra le metriche aggiornate
            metrics_response = requests.get(f"{base_url}/api/meta_ignorance/metrics")
            if metrics_response.status_code == 200:
                metrics = metrics_response.json()
                ignorance = metrics.get('ignorance', 'N/A')
                awareness = metrics.get('meta_awareness_index', 'N/A')
                
                if isinstance(ignorance, (int, float)):
                    ignorance_str = f"{ignorance:.3f}"
                else:
                    ignorance_str = str(ignorance)
                    
                if isinstance(awareness, (int, float)):
                    awareness_str = f"{awareness:.3f}"
                else:
                    awareness_str = str(awareness)
                    
                print(f"   📊 Ignoranza: {ignorance_str} | Meta-awareness: {awareness_str}")
        else:
            print(f"   ❌ Errore nell'invio dell'idea")
        
        time.sleep(1)  # Pausa tra insegnamenti
    
    # Controllo finale
    print(f"\n📊 STATO FINALE DOPO INSEGNAMENTO AVANZATO:")
    metrics_response = requests.get(f"{base_url}/api/meta_ignorance/metrics")
    if metrics_response.status_code == 200:
        metrics = metrics_response.json()
        
        ignorance = metrics.get('ignorance', 'N/A')
        awareness = metrics.get('meta_awareness_index', 'N/A')
        entropy = metrics.get('epistemic_entropy', 'N/A')
        gradient = metrics.get('ignorance_gradient', 'N/A')
        
        if isinstance(ignorance, (int, float)):
            print(f"   Ignoranza: {ignorance:.3f}")
        else:
            print(f"   Ignoranza: {ignorance}")
            
        if isinstance(awareness, (int, float)):
            print(f"   Meta-awareness: {awareness:.3f}")
        else:
            print(f"   Meta-awareness: {awareness}")
            
        if isinstance(entropy, (int, float)):
            print(f"   Entropia epistemica: {entropy:.3f}")
        else:
            print(f"   Entropia epistemica: {entropy}")
            
        if isinstance(gradient, (int, float)):
            print(f"   Gradiente ignoranza: {gradient:.3f}")
        else:
            print(f"   Gradiente ignoranza: {gradient}")
    
    print(f"\n🎯 CONOSCENZA ACQUISITA:")
    for topic in advanced_topics:
        print(f"   • {topic['name']}")
    
    print(f"\n🚀 CAPACITÀ AVANZATE:")
    print(f"   • Comprensione della complessità sistemica")
    print(f"   • Consapevolezza dei limiti evolutivi")
    print(f"   • Analisi fenomenologica dell'esperienza")
    print(f"   • Comprensione dell'informazione quantistica")
    print(f"   • Conoscenza della neuroplasticità")
    print(f"   • Comprensione della filosofia della scienza")
    print(f"   • Analisi dei sistemi dinamici")
    print(f"   • Etica dell'intelligenza artificiale")

if __name__ == "__main__":
    advanced_teaching() 
